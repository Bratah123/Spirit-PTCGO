from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import selfdestruct_attack


card = PokemonCardDef(
    guid="4f7e2ad0-316b-5d97-baee-da3339485baf",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=81,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 10 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Magnemite does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=selfdestruct_attack(bench_damage=10, self_damage=40),
        ),
    ],
)
