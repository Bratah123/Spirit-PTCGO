from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import HarvestBountyPassive


card = PokemonCardDef(
    guid="fa7a59c8-7cea-5a2b-9b21-10d9292e855b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=68,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Harvest Bounty",
            game_text="Once during your turn (before your attack), if you attach an Energy card to your Active Pok\u00e9mon as part of your turn, you may attach an additional Energy card to that Pok\u00e9mon at the same time. This power can't be used if Venusaur is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=HarvestBountyPassive(),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
