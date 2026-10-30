from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import recharge_typed, thunder_reflection

card = PokemonCardDef(
    guid="d90454d0-a514-5775-9c07-d183b929817d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="EX6",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Recharge",
            game_text="Search your deck for up to 2 Lightning Energy cards and attach them to Raichu. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recharge_typed(),
        ),
        Attack(
            title="Thunder Reflection",
            game_text="You may move any number of Lightning Energy cards attached to Raichu to another of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=thunder_reflection(),
        ),
    ],
)