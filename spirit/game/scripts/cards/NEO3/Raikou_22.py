from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    legendary_body_discard_trainers,
    legendary_body_passive,
    overrun,
)


card = PokemonCardDef(
    guid="340da609-2748-56dd-8138-d0496c86b9e2",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raikou.Name",
    display_name="Raikou",
    searchable_by=["Raikou", "Basic", "Raikou"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Ability(
            title="Legendary Body",
            game_text="As long as Raikou is your Active Pok\u00e9mon, Raikou and Energy cards attached to it aren't affected by effects from Trainer cards other than Stadium cards. As long as this Power is active, discard any Trainer cards attached to Raikou. (This power works even if Raikou is Asleep, Confused, or Paralyzed.)",
            ability_type=AbilityTypes.POKE_POWER,
            passive=legendary_body_passive,
            trigger=(Triggers.BETWEEN_TURNS, Triggers.ON_MOVE_TO_ACTIVE),
            effect=legendary_body_discard_trainers,
        ),
        Attack(
            title="Lightning Spark",
            game_text="If your opponent has any Benched Pok\u00e9mon, flip a coin. If heads, choose 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            effect=overrun(20),
        ),
    ],
)
