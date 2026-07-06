from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d2f82d99-9d8c-5515-9e55-76340c1fa395",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    display_name="Cherubi",
    searchable_by=["Cherubi", "Basic", "Cherubi"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=420,
    abilities=[
        Ability(
            title="Lively Fruit",
            game_text="Prevent all effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon. (Damage is not an effect.)",
            effect=unimplemented,
        ),
        Attack(
            title="Leafage",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)