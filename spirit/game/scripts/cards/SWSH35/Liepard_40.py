from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.passives_common import condition_immunity_passive

card = PokemonCardDef(
    guid="3ce55b0b-fde2-51ca-bfa2-c5878146bc43",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard", "Stage 1", "Liepard"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    family_id=509,
    abilities=[
        Ability(
            title="Limber",
            game_text="This Pok\u00e9mon can't be Paralyzed.",
            passive=condition_immunity_passive(SpecialConditions.PARALYZED),
        ),
        Attack(
            title="Slashing Claw",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)