from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="1cb7ebc8-2197-58f4-9edb-143c305912a4",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth δ",
    searchable_by=["Meowth \u03b4", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Pay Day",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=draw_attack(1),
        ),
    ],
)