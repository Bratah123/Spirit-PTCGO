from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import glaring_gaze, no_special_conditions


card = PokemonCardDef(
    guid="9545680a-5b02-5100-9111-c31ea196bb99",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Ability(
            title="Glaring Gaze",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at your opponent's hand. If your opponent has any Trainer cards there, choose 1 of them. Your opponent shuffles that card into his or her deck. This power can't be used if Noctowl is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=no_special_conditions,
            effect=glaring_gaze,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
