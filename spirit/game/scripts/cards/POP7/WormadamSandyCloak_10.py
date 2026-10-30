from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import sandy_cloak_effect_shield, push_over_fighting

card = PokemonCardDef(
    guid="81aea46e-35a3-5632-9eb8-5b0d715f72aa",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamSandyCloak.Name",
    display_name="Wormadam Sandy Cloak",
    searchable_by=['Wormadam Sandy Cloak', 'Stage 1', 'Wormadam'],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmySandyCloak.Name",
    family_id=412,
    abilities=[
        Ability(
            title="Sandy Cloak",
            game_text="Prevent all effects, excluding damage, done to Wormadam Sandy Cloak.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=sandy_cloak_effect_shield(),
            effect=None,
        ),
        Attack(
            title="Push Over",
            game_text="Does 40 damage plus 10 more damage for each Fighting Energy attached to Wormadam Sandy Cloak.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=push_over_fighting(40, 10),
        ),
    ],
)
