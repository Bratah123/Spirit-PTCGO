from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_bench


def _is_passimian(card):
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Passimian"


card = PokemonCardDef(
    guid="69cfff0a-06dd-58e2-9aff-b236962c3217",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name",
    display_name="Passimian",
    searchable_by=["Passimian", "Basic", "Passimian"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=766,
    abilities=[
        Attack(
            title="Fling",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            effect=snipe_attack(30),
        ),
        Attack(
            title="Team Play",
            game_text="This attack does 30 damage for each of your Benched Passimian.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench('mine', pred=_is_passimian), 30, base=10),
        ),
    ],
)