from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.attacks_common import damage_per, count_energy, place_counters


card = PokemonCardDef(
    guid="4e8a8323-cddc-50cc-9af9-6154c2fbc9e6",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonGX.Name",
    display_name="Espeon-GX",
    searchable_by=["Espeon-GX", "Stage 1", "GX", "EspeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=140,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 30, base=60),
        ),
        Attack(
            title="Divide-GX",
            game_text="Put 10 damage counters on your opponent's Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=place_counters(10, 'choose_any_opponent'),
        ),
    ],
)