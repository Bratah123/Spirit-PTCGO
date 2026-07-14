from spirit.game.card_effects.attacks_common import bonus_if, count_energy
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def crescent_glow(ctx):
    """Search a Psychic Energy card and attach it to 1 of your Pokémon (up
    to 3 if you go second and it's your first turn). Then, shuffle."""
    going_second = ctx.player_id != ctx.session.first_player_id
    count = 3 if going_second and ctx.session.turn_state.turn_number == 2 else 1
    picks = await ctx.search_deck(
        lambda c: energy_provides_type(c, PokemonTypes.PSYCHIC.value),
        count=count, minimum=0,
        prompt=f"Choose up to {count} Psychic Energy card(s) to attach.",
    )
    if picks:
        candidates = ctx.my_pokemon_in_play()
        if candidates:
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if target is not None:
                for card in picks:
                    await ctx.attach_energy(card, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="968e81cc-ca14-5d20-9bd6-2a27a11f66c0",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=228,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=488,
    abilities=[
        Attack(
            title="Crescent Glow",
            game_text="Search your deck for a Psychic Energy card and attach it to 1 of your Pok\u00e9mon. If you go second and it's your first turn, instead search for up to 3 Psychic Energy cards and attach them to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=crescent_glow,
        ),
        Attack(
            title="Photon Laser",
            game_text="If you have at least 5 Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: count_energy("mine")(ctx) >= 5, 90),
        ),
    ],
)