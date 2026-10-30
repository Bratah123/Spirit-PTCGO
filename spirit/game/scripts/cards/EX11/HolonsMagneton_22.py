"""EX11 Delta Species — Holon dual-mode Energy attach.
"""
from spirit.game.card_effects.ex import holon_stage1_energy_on_attach, holon_pokemon_energy_attach_to_with_energy
from spirit.game.card_effects.energies import ALL_TYPES_TWO_AT_A_TIME
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import extra_ball_vs_ex
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a568645-190a-5268-8fa4-28e59b91e31d",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsMagneton.Name",
    display_name="Holon's Magneton",
    searchable_by=["Holon's Magneton", "Stage 1", "HolonsMagneton"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HolonsMagnemite.Name",
    family_id=81,
    attachable_as_energy=True,
    energy_provides=ALL_TYPES_TWO_AT_A_TIME,
    energy_attach_to=holon_pokemon_energy_attach_to_with_energy,
    energy_on_attach=holon_stage1_energy_on_attach,
    abilities=[
        Attack(
            title="Extra Ball",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=extra_ball_vs_ex(30, 20),
        ),
    ],
)