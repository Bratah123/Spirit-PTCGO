from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="781ab9ae-de27-5427-90f5-3de9a776b81f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic", "Darumaka"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)