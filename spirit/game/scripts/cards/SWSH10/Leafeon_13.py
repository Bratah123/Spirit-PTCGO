from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def energy_garden(ctx):
    """Search for up to 3 basic Energy of different types and attach them freely; shuffle."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
    if reps:
        picks = await ctx.choose_cards(
            reps, 3, minimum=0,
            prompt="Choose up to 3 basic Energy cards of different types.",
            display_cards=deck_cards,
        )
        for energy in picks:
            target = await ctx.choose_pokemon(
                ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to"
            )
            if target is not None:
                await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


async def leafy_cyclone(ctx):
    """120 damage; this Pokémon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="40c6ef9d-605f-5519-8a8b-b0e685b89145",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1", "Leafeon"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Energy Garden",
            game_text="Search your deck for up to 3 basic Energy cards of different types and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=energy_garden,
        ),
        Attack(
            title="Leafy Cyclone",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=leafy_cyclone,
        ),
    ],
)