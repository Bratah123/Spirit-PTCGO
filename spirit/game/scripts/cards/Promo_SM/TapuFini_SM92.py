from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.smp import shining_current


card = PokemonCardDef(
    guid="c0b9a0e8-0228-5dfa-b3fa-9a8bdfa08705",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuFini.Name",
    display_name="Tapu Fini",
    searchable_by=["Tapu Fini", "Basic", "TapuFini"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=788,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Shining Current",
            game_text="If any of your Water Pok\u00e9mon was healed during this turn, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=shining_current,
        ),
    ],
)