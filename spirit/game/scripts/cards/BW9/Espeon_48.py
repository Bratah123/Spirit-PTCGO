from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_until_effect
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="fa5dadd8-dab7-59d0-a130-544923db050b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Team Plasma", "Espeon"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=48,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Psy Alert",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=draw_until_effect(6),
        ),
        Attack(
            title="Shadow Ball",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. Also apply Weakness and Resistance for Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=snipe_attack(40, pool='any', apply_modifiers=True),
        ),
    ],
)