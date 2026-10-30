from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.ex import (
    copy_supporter_from_opponent_hand, may_discard_energy_for_condition,
)


card = PokemonCardDef(
    guid="fb669ac0-b0bd-53a1-a459-cd35531a0582",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=302,
    abilities=[
        Attack(
            title="Supernatural",
            game_text="Look at your opponent's hand. You may use the effect of a Supporter card you find there as the effect of this attack. (The Supporter card remains in your opponent's hand.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_supporter_from_opponent_hand,
        ),
        Attack(
            title="Dark Bind",
            game_text="You may discard a Darkness Energy card attached to Sableye. If you do, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=may_discard_energy_for_condition(
                PokemonTypes.DARKNESS, SpecialConditions.PARALYZED,
                prompt="You may discard a Darkness Energy card",
            ),
        ),
    ],
)
