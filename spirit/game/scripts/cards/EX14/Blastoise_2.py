from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import enraged_linear_attack, shield_veil_active_no_weakness

card = PokemonCardDef(
    guid="d83aa82d-57b6-53b8-a646-fbdb04feab30",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise δ",
    searchable_by=["Blastoise \u03b4", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX14",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Shield Veil",
            game_text="Each of your Active Pok\u00e9mon has no Weakness.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=shield_veil_active_no_weakness(),
            effect=None,
        ),
        Attack(
            title="Enraged Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage for each damage counter on Blastoise to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
                        effect=enraged_linear_attack(10),
        ),
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)