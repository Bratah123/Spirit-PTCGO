from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.hf import last_pattern, rocket_tail

card = PokemonCardDef(
    guid="f7d31cd5-1fef-5210-a9fa-36d6ffee2777",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="HF",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Ability(
            title="Last Pattern",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an opponent's attack, discard 2 random cards from your opponent's hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=last_pattern,
        ),
        Attack(
            title="Rocket Tail",
            game_text="If Jessie & James is in your discard pile, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=rocket_tail,
        ),
    ],
)
