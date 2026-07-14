from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_prizes_taken

card = PokemonCardDef(
    guid="34cd3966-5bc2-508d-868e-c49c4b32005c",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashVMAX.Name",
    display_name="Aegislash VMAX",
    searchable_by=["Aegislash VMAX", "VMAX", "AegislashVMAX"],
    subtypes=["VMAX"],
    collector_number=127,
    set_code="SWSH4",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashV.Name",
    family_id=681,
    abilities=[
        Attack(
            title="Max Hack",
            game_text="This attack does 30 more damage for each Prize card you have taken.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("mine"), 30, base=160),
        ),
    ],
)