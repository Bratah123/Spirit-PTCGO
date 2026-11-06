from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    revive_friends,
    revive_friends_condition,
    work_together,
)


card = PokemonCardDef(
    guid="0878618a-4d98-5fe7-93df-46bce293a60a",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Revive Friends",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card named Kabuto and put it on your Bench. Shuffle your deck afterward. Treat the new Kabuto as a Basic Pok\u00e9mon. This power can't be used if Kabuto is Asleep, Confused, or Paralyzed (or if your Bench is full).",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=revive_friends_condition,
            effect=revive_friends,
        ),
        Attack(
            title="Work Together",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage for each Omanyte, Omastar, Kabuto, and Kabutops on your Bench.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=work_together,
        ),
    ],
)
