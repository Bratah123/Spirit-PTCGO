from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.card_effects.trainers import is_dragon_pokemon


card = PokemonCardDef(
    guid="0a97fa99-05bb-53f3-83e2-d1a0e2862424",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    display_name="Fraxure",
    searchable_by=["Fraxure", "Stage 1", "Fraxure"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Dragon Slayer",
            game_text="If your opponent's Active Pok\u00e9mon is a Dragon Pok\u00e9mon, this attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.opponent_active() is not None and is_dragon_pokemon(ctx.opponent_active()), 40),
        ),
    ],
)