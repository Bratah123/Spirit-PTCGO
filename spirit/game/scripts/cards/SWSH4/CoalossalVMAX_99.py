from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5a593a19-bc43-5a7e-a1e7-1d243b7a7a40",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CoalossalVMAX.Name",
    display_name="Coalossal VMAX",
    searchable_by=["Coalossal VMAX", "VMAX", "CoalossalVMAX"],
    subtypes=["VMAX"],
    collector_number=99,
    set_code="SWSH4",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CoalossalV.Name",
    family_id=839,
    abilities=[
        Attack(
            title="Eruption Shot",
            game_text="Discard the top card of your deck. If that card is an Energy card, this attack does 90 more damage, and attach that card to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Boulder",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
        ),
    ],
)