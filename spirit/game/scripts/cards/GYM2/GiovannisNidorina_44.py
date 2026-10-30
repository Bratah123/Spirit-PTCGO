from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, recoil_attack


card = PokemonCardDef(
    guid="c8dd1ffb-9989-5e71-8dd1-ea0586aa955f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidorina.Name",
    display_name="Giovanni's Nidorina",
    searchable_by=["Giovanni's Nidorina", "Stage 1", "GiovannisNidorina"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisNidoran.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Poison Sting Tackle",
            game_text="Giovanni's Nidorina does 20 damage to itself. Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(
                20,
                also=condition_attack(SpecialConditions.POISONED, flip=True, damage=0),
            ),
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
