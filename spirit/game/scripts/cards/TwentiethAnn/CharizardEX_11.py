from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.attacks_common import flip_damage


def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


card = PokemonCardDef(
    guid="d3739a5b-de0a-565f-8c91-714d293da945",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    display_name="Charizard-EX",
    searchable_by=["Charizard-EX", "Basic", "EX", "CharizardEX"],
    subtypes=["Basic", "EX"],
    collector_number=11,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=attach_from_discard(predicate=_is_fire_energy),
        ),
        Attack(
            title="Burning Breath",
            game_text="Flip 2 coins. This attack does 40 more damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=40),
        ),
    ],
)