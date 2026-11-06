from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


card = PokemonCardDef(
    guid="afc071de-f52b-5294-8d35-e0e1c8beeda5",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EnteiEX.Name",
    display_name="Entei-EX",
    searchable_by=["Entei-EX", "Basic", "EX", "EnteiEX"],
    subtypes=["Basic", "EX"],
    collector_number=103,
    set_code="BW5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Grand Flame",
            game_text="Attach a Fire Energy from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=attach_from_discard(
                predicate=_is_fire_energy, count=1,
                target=lambda p: not is_in_active_spot(p),
                prompt='Choose a Fire Energy card to attach to 1 of your Benched Pokémon.'),
        ),
    ],
)