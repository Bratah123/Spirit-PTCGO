from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="462eac11-e0a8-51ea-8787-84ea97eb68f7",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BoltundV.Name",
    display_name="Boltund V",
    searchable_by=["Boltund V", "Basic", "V", "BoltundV"],
    subtypes=["Basic", "V"],
    collector_number=249,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=836,
    abilities=[
        Attack(
            title="Smash Turn",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Electrobullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)