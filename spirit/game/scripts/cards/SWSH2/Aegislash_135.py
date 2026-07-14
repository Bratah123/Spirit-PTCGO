from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonCardDef(
    guid="078d1bb9-3aef-5095-990d-46022d273fed",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Big Shield",
            game_text="All of your Pok\u00e9mon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance). You can't apply more than 1 Big Shield Ability at a time.",
            passive=takes_less_passive(30, protects="team", stack_key="BigShield"),
        ),
        Attack(
            title="Power Edge",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)