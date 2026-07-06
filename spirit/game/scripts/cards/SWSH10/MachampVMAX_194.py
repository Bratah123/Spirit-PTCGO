from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30f60ece-43ec-5581-9836-51e31176b8a3",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampVMAX.Name",
    display_name="Machamp VMAX",
    searchable_by=["Machamp VMAX", "VMAX", "MachampVMAX"],
    subtypes=["VMAX"],
    collector_number=194,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MachampV.Name",
    family_id=68,
    abilities=[
        Attack(
            title="Revenge Buster",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Chi Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use G-Max Chi Strike.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            effect=unimplemented,
        ),
    ],
)