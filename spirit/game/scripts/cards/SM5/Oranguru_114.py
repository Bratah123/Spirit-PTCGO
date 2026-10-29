from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm5 import resource_management

card = PokemonCardDef(
    guid="6d2c6935-a03a-54f3-8548-6910317124ec",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic", "Oranguru"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Attack(
            title="Resource Management",
            game_text="Put 3 cards from your discard pile on the bottom of your deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=resource_management,
        ),
        Attack(
            title="Profound Knowledge",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)