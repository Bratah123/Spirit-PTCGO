from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import double_named_attack_next_turn


card = PokemonCardDef(
    guid="9be7c038-f068-59b0-8aab-111c39be219a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesRattata.Name",
    display_name="Lt. Surge's Rattata",
    searchable_by=["Lt. Surge's Rattata", "Basic", "LtSurgesRattata"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=19,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Lt. Surge's Rattata's Quick Attack's base damage is doubled.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=double_named_attack_next_turn("Quick Attack", 10),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
