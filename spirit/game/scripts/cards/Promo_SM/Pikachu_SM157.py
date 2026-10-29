from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.passives_common import condition_immunity_passive


card = PokemonCardDef(
    guid="ca6e3ebb-9758-5c68-9a85-93fa00679c1b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Ability(
            title="Pika Shield",
            game_text="This Pok\u00e9mon can't be Paralyzed.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=condition_immunity_passive(SpecialConditions.PARALYZED),
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)