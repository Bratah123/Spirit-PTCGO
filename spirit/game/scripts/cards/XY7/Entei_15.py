from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="620728d0-9fb3-556b-839d-56f0bd46065f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        ancient_trait('θ Double'),
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Heat Tackle",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=flip_damage(tails_self_damage=30),
        ),
    ],
)