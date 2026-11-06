from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import reduce_if_defending_attacks


card = PokemonCardDef(
    guid="d363a296-6c60-56eb-b803-de2dd990c022",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Growl",
            game_text="If the Defending Pok\u00e9mon attacks Pikachu during your opponent's next turn, any damage done by the attack is reduced by 10 (after applying Weakness and Resistance). (Benching either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=reduce_if_defending_attacks(10),
        ),
        Attack(
            title="Thundershock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
