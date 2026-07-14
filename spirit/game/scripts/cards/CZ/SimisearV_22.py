from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d876a79c-0f49-508d-a68d-c883e02733f1",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SimisearV.Name",
    display_name="Simisear V",
    searchable_by=["Simisear V", "Basic", "V", "SimisearV"],
    subtypes=["Basic", "V"],
    collector_number=22,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=514,
    abilities=[
        Attack(
            title="Bursting Power",
            game_text="You may attach up to 2 basic Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Flare Juggling",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)