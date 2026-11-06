from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


card = PokemonCardDef(
    guid="346a9848-5ff3-5c9b-a516-cd3b4208ff0a",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomEX.Name",
    display_name="Houndoom-EX",
    searchable_by=["Houndoom-EX", "Basic", "EX", "HoundoomEX"],
    subtypes=["Basic", "EX"],
    collector_number=153,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=229,
    abilities=[
        Attack(
            title="Melting Horn",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=mill_attack(2),
        ),
        Attack(
            title="Grand Flame",
            game_text="Attach a Fire Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            effect=attach_from_discard(predicate=_is_fire_energy, count=1, target=lambda p: not is_in_active_spot(p), prompt='Choose a Fire Energy card to attach to 1 of your Benched Pokémon.'),
        ),
    ],
)