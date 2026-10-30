from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import attack_effect_shield_passive


card = PokemonCardDef(
    guid="f5030c5c-6181-5ff6-9e4e-3ecf94327a3e",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Protective Dust",
            game_text="Prevent all effects of attacks, except damage, done to Dustox by the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Toxic",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, counters=2),
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
