from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import carry_off, carry_off_condition, double_cross


card = PokemonCardDef(
    guid="6caf0b46-9ff0-5679-9976-c460d8aec328",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=155,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Carry Off",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at your opponent's hand. If your opponent has any Baby Pok\u00e9mon, Basic Pok\u00e9mon, or Evolution cards there, choose 1 of them. Your opponent shuffles that card into his or her deck. This power can't be used if Crobat is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=carry_off_condition,
            effect=carry_off,
        ),
        Attack(
            title="Double Cross",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads. If both of them are tails, the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=double_cross,
        ),
    ],
)
