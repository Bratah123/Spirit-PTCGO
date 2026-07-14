from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.passives_common import retreat_free_when


def _vamoose(pokemon, carrier):
    if pokemon is not carrier:
        return False
    max_hp = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0)
    )
    return pokemon.get_attribute(AttrID.HP, 0) < max_hp


card = PokemonCardDef(
    guid="6b14cf73-53b8-5f9c-acfc-234ea47d5a32",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=185,
    abilities=[
        Ability(
            title="Vamoose",
            game_text="If this Pok\u00e9mon has any damage counters on it, it has no Retreat Cost.",
            passive=retreat_free_when(_vamoose),
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=90,
            effect=recoil_attack(30),
        ),
    ],
)