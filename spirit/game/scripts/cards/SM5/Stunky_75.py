from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="24d78df8-f592-539c-ad3f-17511532ba6b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    display_name="Stunky",
    searchable_by=["Stunky", "Basic", "Stunky"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=434,
    abilities=[
        Attack(
            title="Gas Bond",
            game_text="Both Active Pok\u00e9mon are now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED, both_actives=True),
        ),
    ],
)