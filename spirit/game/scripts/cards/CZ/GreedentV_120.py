from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="aab2eb28-3de4-5543-80f3-f25e0ebbbbe9",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreedentV.Name",
    display_name="Greedent V",
    searchable_by=["Greedent V", "Basic", "V", "GreedentV"],
    subtypes=["Basic", "V"],
    collector_number=120,
    set_code="CZ",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=820,
    abilities=[
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Nom-Nom-Nom Incisors",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=draw_attack(3),
        ),
    ],
)