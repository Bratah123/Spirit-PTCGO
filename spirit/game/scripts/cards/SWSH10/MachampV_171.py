from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9f074faa-8e18-534a-86d8-570653e94688",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampV.Name",
    display_name="Machamp V",
    searchable_by=["Machamp V", "Basic", "V", "MachampV"],
    subtypes=["Basic", "V"],
    collector_number=171,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=68,
    abilities=[
        Attack(
            title="Revenge Buster",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)