from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ff1506b8-e3ef-55dd-b581-886e148c0113",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=701,
    abilities=[
        Attack(
            title="Backflip",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Wicked Jab",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)