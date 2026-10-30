from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import bustle_flip_confuse


card = PokemonCardDef(
    guid="fb642272-a358-586e-ad4e-5d05efe1f019",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PichuBros.Name",
    display_name="Pichu Bros.",
    searchable_by=["Pichu Bros.", "Basic", "PichuBros"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="POP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Bustle",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads. If either coin is heads, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
            damage_operator="×",
            effect=bustle_flip_confuse(2, 20),
        ),
    ],
)
