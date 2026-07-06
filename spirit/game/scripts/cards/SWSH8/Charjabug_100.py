from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c2d552a-ed75-5b9e-9684-9b28746e9d1a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    display_name="Charjabug",
    searchable_by=["Charjabug", "Stage 1", "Charjabug"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    family_id=736,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)