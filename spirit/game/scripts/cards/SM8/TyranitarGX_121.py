from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import ignore_effects_attack

from spirit.game.card_effects.sm8 import (
    dusty_ruckus,
    lost_out_passive,
)

card = PokemonCardDef(
    guid="bfdc485c-c4ec-5d17-8216-dcbda2b93831",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarGX.Name",
    display_name="Tyranitar-GX",
    searchable_by=["Tyranitar-GX", "Stage 2", "GX", "TyranitarGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=121,
    set_code="SM8",
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Lost Out",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this Pok\u00e9mon's attacks, put that Pok\u00e9mon and all cards attached to it in the Lost Zone instead of the discard pile.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=lost_out_passive
        ),
        Attack(
            title="Dusty Ruckus",
            game_text="This attack does 30 damage to each of your opponent's Benched Basic Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=dusty_ruckus
        ),
        Attack(
            title="Lay the Smackdown-GX",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=ignore_effects_attack(),
        ),
    ],
)