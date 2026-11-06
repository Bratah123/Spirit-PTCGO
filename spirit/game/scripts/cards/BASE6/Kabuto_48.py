from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import kabuto_armor


card = PokemonCardDef(
    guid="6b8753f4-e288-5867-85f5-72f18736d5b5",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    display_name="Kabuto",
    searchable_by=["Kabuto", "Stage 1", "Kabuto"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Kabuto Armor",
            game_text="Whenever an attack (even your own) does damage to Kabuto (after applying Weakness and Resistance), that attack does only half the damage to Kabuto (rounded down to the nearest 10). (Any other effects of attacks still happen.) This power stops working while Kabuto is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=kabuto_armor,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
