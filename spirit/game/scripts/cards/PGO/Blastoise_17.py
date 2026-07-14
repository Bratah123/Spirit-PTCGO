from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.attacks_common import damage_per, count_energy

_vitality_spring_search = search_attach_energy(count=6, distribute=True, shuffle=True)


async def vitality_spring(ctx):
    """Once during your turn, you may search up to 6 Energy and attach them
    in any way you like. If you do, your turn ends."""
    if await ctx.ask_yes_no(
        "Search your deck for up to 6 Energy cards and attach them to "
        "your Pokémon in any way you like?"
    ):
        await _vitality_spring_search(ctx)
        ctx.ends_turn = True


card = PokemonCardDef(
    guid="49dab7f1-a23f-5747-954d-9305cf47d5df",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Vitality Spring",
            game_text="Once during your turn, you may search your deck for up to 6 Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            effect=vitality_spring,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 30 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator="+",
            effect=damage_per(
                count_energy("self", energy_type=PokemonTypes.WATER), 30, base=90
            ),
        ),
    ],
)