from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="cc512e9e-f3e4-543e-8f0d-042559edae70",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emboar.Name",
    display_name="Emboar",
    searchable_by=["Emboar", "Stage 2", "Emboar"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="BW1",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=self_energy_discard_attack(
                all_energy=True, energy_type=PokemonTypes.FIRE
            ),
        ),
    ],
)
