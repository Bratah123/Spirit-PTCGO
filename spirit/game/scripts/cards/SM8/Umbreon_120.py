from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="03ffef9f-fb93-5550-8bea-e74e30235438",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Umbreon"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.kos_suffered_last_turn() > 0, 90),
        ),
        Attack(
            title="Dark Cutter",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)