from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    AttrID, CLIENT_POKEMON_TYPE_NAMES, PokemonTypes, PokemonStage, Rarities,
)
from spirit.game.card_effects.trainers import is_basic_energy_card


async def breath_of_life(ctx):
    """Search up to 3 basic Energy of different types and attach them to your
    Pokémon in any way you like. Then, shuffle your deck."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    labels = {}
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
        labels[card.entity_id] = f"{CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(types[0])]} Energy"

    # No matches still shows the deck browser (nothing selectable).
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    for energy in picks:
        label = labels[energy.entity_id]
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), f"Choose a Pokémon to attach {label} to"
        )
        if target is not None:
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="bf180f7a-320b-507f-80e6-dede7ace3b13",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="CEL25",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Breath of Life",
            game_text="Search your deck for up to 3 basic Energy cards of different types and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=breath_of_life,
        ),
        Attack(
            title="Aurora Horns",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)