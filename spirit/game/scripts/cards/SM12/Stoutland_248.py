from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm8 import lava_burn
from spirit.game.card_effects.sm12 import arf_arf_bark


card = PokemonCardDef(
    guid="ec801e44-e1c8-5c4c-be84-2b1cd245e141",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name",
    display_name="Stoutland",
    searchable_by=["Stoutland", "Stage 2", "Stoutland"],
    subtypes=["Stage 2"],
    collector_number=248,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name",
    family_id=506,
    abilities=[
        Ability(
            title="Arf Arf Bark",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard an Energy from your opponent's Active Pok\u00e9mon. If this Pok\u00e9mon is your Active Pok\u00e9mon and is Knocked Out by damage from an opponent's attack, you may discard an Energy from your opponent's Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=(Triggers.ON_EVOLVE, Triggers.ON_KNOCKED_OUT),
            effect=arf_arf_bark,
        ),
        Attack(
            title="Overrun",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=lava_burn,
        ),
    ],
)