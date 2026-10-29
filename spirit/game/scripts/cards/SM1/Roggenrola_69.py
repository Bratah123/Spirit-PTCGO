from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _has_fighting_resistance(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and \
        defender.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value


card = PokemonCardDef(
    guid="790222fa-58ef-5b5b-9495-e44455e030af",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic", "Roggenrola"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Smack Down",
            game_text="If your opponent's Active Pok\u00e9mon has Fighting Resistance, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(_has_fighting_resistance, 50),
        ),
    ],
)