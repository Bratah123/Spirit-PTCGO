from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import attack_effect_shield_passive

card = PokemonCardDef(
    guid="084dbd4e-a047-5b48-af4e-1d83ac9a5721",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Ability(
            title="Unaware",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to this Pok\u00e9mon.",
            passive=attack_effect_shield_passive(),
        ),
        Attack(
            title="Heart Stamp",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)